"""
Metadata são dados internos

"""

from importlib import metadata

# Versão do pip
print(metadata.version('pip'))

# Quais são os metadados disponiveis
metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))


# Quantos pacotes tem no pip?
print(len(metadata.files('pip')))

# O que o pip requer?
print(metadata.requires("pip"))
