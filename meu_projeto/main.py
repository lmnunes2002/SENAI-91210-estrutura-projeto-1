import os
from models.funcionarios import Funcionario
from models.enums.setor import Setor
from models.enums.sexo import Sexo

os.system("cls||clear")

funcionario_1 = Funcionario(123, "Lucas", 22, 4000.0, Setor.VENDAS, Sexo.MASCULINO)
print(funcionario_1)