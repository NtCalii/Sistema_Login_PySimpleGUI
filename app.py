import PySimpleGUI as sg
from sqlalchemy.exc import SQLAlchemyError
from janelas import *
from models import Usuario
from bd import Base, session, db
import hashlib

janela_logar, janela_cadastrar, janela_principal = janela_login(), None, None

while True:
    Base.metadata.create_all(bind=db)
    window, evento, valores = sg.read_all_windows()
    if evento == sg.WINDOW_CLOSED:
        break

    def hash(txt):
        hash_obj = hashlib.sha256(txt.encode("utf-8"))
        return hash_obj.hexdigest()

    if window == janela_logar and evento == "Logar":
        try:
            email = valores["email_usuario"].strip()
            senha = valores["senha_usuario"].strip()

            if not email or not senha:
                sg.popup_error("ERRO! A senha e email são obrigatórios para entrar.")
                continue

            usuario = session.query(Usuario).filter_by(email=email).first()

            if not usuario:
                sg.popup_error("Usuário não encontrado!")
                continue

            senha_hash = hash(senha)
            if usuario.senha != senha_hash:
                sg.popup_error("Senha incorreta!")
                continue

            janela_logar.close()
            janela_principal = janela_inicial(usuario.nome)

        except SQLAlchemyError as e:
            session.rollback()
            sg.popup_error(f"Erro no banco de dados:\n{e}")
        except Exception as e:
            sg.popup_error(f"Erro inesperado:\n{e}")

    if window == janela_logar and evento == "Cadastre-se":
        janela_cadastrar = janela_cadastro()
        janela_logar.hide()

    if window == janela_cadastrar and evento == "Cadastrar":
        try:
            nome = valores["nome_usuario"].strip()
            email = valores["email_usuario"].strip()
            senha = valores["senha_usuario"].strip()
            confirmacao_senha = valores["confirmacao_senha_usuario"].strip()

            if not nome or not email or not senha:
                sg.popup_error("ERRO! Todos os campos são obrigatórios.")
                continue

            if confirmacao_senha != senha:
                sg.popup_error("ERRO! Senhas são diferentes uma da outra.")
                continue

            novo_usuario = Usuario(nome, email, hash(senha))
            session.add(novo_usuario)
            session.commit()

            janela_logar.un_hide()
            janela_cadastrar.close()
        except SQLAlchemyError as e:
            session.rollback()
            sg.popup("Erro! ao criar novo usuário.\n"
                     f"Detalhes: {e}")
