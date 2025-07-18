import PySimpleGUI as sg

def janela_login():
    sg.theme("Dark")
    layout = [
        [sg.Text("Email: "), sg.Input("", key="email_usuario", size=(25, 1))],
        [sg.Text("Senha: "), sg.Input("", key="senha_usuario", size=(25, 1),
                                      password_char="*")],
        [sg.Button("Logar")],
        [sg.Text("Não tem cadastro?"), sg.Button("Cadastre-se")]
    ]
    return sg.Window("Login", layout=layout, finalize=True)

def janela_cadastro():
    sg.theme("Dark")
    layout = [
        [sg.Text("Nome: "), sg.Input("", key="nome_usuario", size=(25, 1))],
        [sg.Text("Email: "), sg.Input("", key="email_usuario", size=(25, 1))],
        [sg.Text("Senha: "), sg.Input("", key="senha_usuario", size=(25, 1),
                                      password_char="*")],
        [sg.Text("Confirme sua Senha: "), sg.Input("", key="confirmacao_senha_usuario",
                                                       size=(20, 1), password_char="*")],
        [sg.Button("Cadastrar")]
    ]
    return sg.Window("Cadastro", layout=layout, finalize=True)

def janela_inicial(nome):
    sg.theme("Dark")
    layout = [
        [sg.Text(f"Olá {nome}")]
    ]
    return  sg.Window("Página Inicial", layout=layout, finalize=True)
