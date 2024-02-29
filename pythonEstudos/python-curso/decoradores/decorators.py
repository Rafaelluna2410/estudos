'''

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- São também exemplos de Higher Order Functions
- tem uma sintaxe própria, usando @

/-----------------------------------------------\ 
/               Function Decorator              \
/-----------------------------------------------\



-----------------------------------------------------
| /-----------------------------------------------\ |
| /               Function decorada               \ |
| /-----------------------------------------------\ |
-----------------------------------------------------

# decorator como funções usando sintaxe não recomendada

# 1

def seja_educado(funcao):
    def sendo():
        print('foi um prazer conhecer você')
        funcao()
        print('tenha um ótima dia')
    return sendo

def saudacao():
    print('Seja bem-vindo')

teste = seja_educado(saudacao)

teste()

'''

# 2 sintaxe recomendada 

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()