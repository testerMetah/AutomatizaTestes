"""Conferência parametrizada de reservas no banco do Acessus, sem gravar dados."""
from datetime import datetime


def query_spec(filters):
    allowed = {'credencial', 'id_refeitorio', 'id_empresa', 'inicio', 'termino', 'id_exportacao', 'refeicoes', 'situacao', 'status'}
    if not isinstance(filters, dict) or set(filters) - allowed:
        raise ValueError('Filtros de reserva inválidos.')
    if not {'credencial', 'id_refeitorio', 'id_empresa', 'inicio', 'termino'} <= filters.keys():
        raise ValueError('Reserva exige credencial, id_refeitorio, id_empresa, inicio e termino confirmados no Acessus.')
    for key in ('id_refeitorio', 'id_empresa'):
        if type(filters[key]) is not int or filters[key] <= 0:
            raise ValueError(key + ' deve ser um ID interno positivo do Acessus.')
    for key in ('situacao', 'status'):
        if key in filters and (type(filters[key]) is not int or filters[key] < 0):
            raise ValueError(key + ' deve ser um inteiro não negativo confirmado.')
    for key in ('credencial', 'id_exportacao', 'refeicoes'):
        if key in filters and (not isinstance(filters[key], str) or not filters[key].strip()):
            raise ValueError(key + ' precisa ser um texto não vazio confirmado.')
    dates = []
    for key in ('inicio', 'termino'):
        if not isinstance(filters[key], str) or 'T' not in filters[key]:
            raise ValueError('Use data e hora ISO completas nas expectativas de reserva.')
        try:
            value = datetime.fromisoformat(filters[key])
        except ValueError:
            raise ValueError('Data/hora de reserva inválida.') from None
        if value.tzinfo is not None:
            raise ValueError('Use o horário local sem fuso armazenado no SQL Server.')
        dates.append(value)
    if dates[1] < dates[0]:
        raise ValueError('Término da reserva anterior ao início.')
    clauses = ['credencial = ?', 'id_refeitorio = ?', 'id_empresa = ?', 'datahoraini = ?', 'datahorafim = ?']
    params = [filters['credencial'], filters['id_refeitorio'], filters['id_empresa'], *dates]
    for key, column in [('id_exportacao', 'IdExportacao'), ('refeicoes', 'refeicoes')]:
        if key in filters:
            clauses.append(column + ' = ?')
            params.append(filters[key])
    for key in ('situacao', 'status'):
        if key in filters:
            clauses.append(key + ' = ?')
            params.append(filters[key])
    sql = ('SET LOCK_TIMEOUT 1000; SET DEADLOCK_PRIORITY LOW; '
           'SELECT TOP (101) id, credencial, id_refeitorio, IdExportacao, '
           'refeicoes, datahoraini, datahorafim, situacao, status, id_empresa '
           'FROM dbo.RefeicoesReservas WHERE ' + ' AND '.join(clauses) + ' ORDER BY id')
    return sql, tuple(params), 100
