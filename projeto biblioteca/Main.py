"""
╔══════════════════════════════════════════════════════╗
║         SISTEMA DE BIBLIOTECA — INTERFACE GRÁFICA    ║
║         PyQt5 — versão PROCEDURAL (sem classes)       ║
╚══════════════════════════════════════════════════════╝

ATENÇÃO: Este arquivo é apenas o FRONT-END (interface visual).
Nenhuma lógica de DAO ou banco de dados foi alterada.
Qualquer integração futura deve ser aprovada antes de implementar.

Esta versão mantém exatamente a mesma aparência da versão original,
mas troca as classes (CardAcao, PaginaSecao, MenuLateral, JanelaPrincipal)
por funções que constroem e devolvem os widgets. QMainWindow e QWidget
são usados diretamente (instanciados), sem criar subclasses próprias.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QStackedWidget, QFrame, QScrollArea
)
from PyQt5.QtCore import Qt


# ─────────────────────────────────────────────────────
# PALETA DE CORES — altere aqui para mudar o tema geral
# ─────────────────────────────────────────────────────
CORES = {
    "fundo":          "#0F1117",   # fundo principal (quase preto)
    "painel":         "#1A1D27",   # fundo dos cards/painéis
    "borda":          "#2A2D3E",   # linhas divisórias e bordas
    "primaria":       "#6C63FF",   # roxo elétrico — cor de destaque principal
    "primaria_hover": "#8B85FF",   # versão mais clara ao passar o mouse
    "secundaria":     "#FF6584",   # rosa/coral — acento secundário
    "texto":          "#E8E8F0",   # texto principal (quase branco)
    "texto_suave":    "#8A8AA0",   # texto secundário / subtítulos
    "sucesso":        "#43D9AD",   # verde para confirmações
    "alerta":         "#FFB86C",   # laranja para avisos
    "erro":           "#FF5555",   # vermelho para erros
}

# ─────────────────────────────────────────────────────
# ESTILOS GLOBAIS (QSS = Qt Style Sheets, similar ao CSS)
# ─────────────────────────────────────────────────────
ESTILO_GLOBAL = f"""
    QMainWindow, QWidget {{
        background-color: {CORES['fundo']};
        color: {CORES['texto']};
        font-family: 'Segoe UI', 'Ubuntu', sans-serif;
    }}

    QPushButton#btn_menu {{
        background-color: transparent;
        color: {CORES['texto_suave']};
        border: none;
        border-left: 3px solid transparent;
        padding: 14px 20px;
        text-align: left;
        font-size: 14px;
        border-radius: 0px;
    }}
    QPushButton#btn_menu:hover {{
        background-color: {CORES['borda']};
        color: {CORES['texto']};
        border-left: 3px solid {CORES['primaria']};
    }}
    QPushButton#btn_menu:checked {{
        background-color: {CORES['borda']};
        color: {CORES['primaria']};
        border-left: 3px solid {CORES['primaria']};
        font-weight: bold;
    }}

    QPushButton#btn_acao {{
        background-color: {CORES['primaria']};
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 22px;
        font-size: 13px;
        font-weight: bold;
    }}
    QPushButton#btn_acao:hover {{
        background-color: {CORES['primaria_hover']};
    }}
    QPushButton#btn_acao:pressed {{
        background-color: {CORES['primaria']};
        padding-top: 12px;
    }}

    QFrame#separador {{
        background-color: {CORES['borda']};
        max-height: 1px;
    }}

    QScrollArea {{
        background-color: transparent;
        border: none;
    }}
    QScrollBar:vertical {{
        background: {CORES['painel']};
        width: 6px;
        border-radius: 3px;
    }}
    QScrollBar::handle:vertical {{
        background: {CORES['primaria']};
        border-radius: 3px;
    }}
"""

# ─────────────────────────────────────────────────────
# ESTADO GLOBAL — preenchido dentro de construir_janela()
# ─────────────────────────────────────────────────────
janela = None
paginas = None       # QStackedWidget com as seções
botoes_menu = []      # lista de botões do menu lateral (pra marcar o ativo)


# ══════════════════════════════════════════════════════
# CARD DE AÇÃO — cada operação disponível dentro de uma seção
# ══════════════════════════════════════════════════════
def criar_card_acao(titulo: str, descricao: str, cor_icone: str = None) -> QFrame:
    cor = cor_icone or CORES["primaria"]

    card = QFrame()
    card.setStyleSheet(f"""
        QFrame {{
            background-color: {CORES['painel']};
            border: 1px solid {CORES['borda']};
            border-radius: 10px;
            padding: 4px;
        }}
        QFrame:hover {{
            border: 1px solid {cor};
        }}
    """)
    card.setFixedHeight(80)

    layout = QHBoxLayout(card)
    layout.setContentsMargins(16, 12, 16, 12)
    layout.setSpacing(14)

    indicador = QLabel("●")
    indicador.setStyleSheet(f"color: {cor}; font-size: 18px;")
    indicador.setFixedWidth(24)

    coluna_texto = QVBoxLayout()
    coluna_texto.setSpacing(2)

    lbl_titulo = QLabel(titulo)
    lbl_titulo.setStyleSheet(f"""
        color: {CORES['texto']};
        font-size: 14px;
        font-weight: bold;
        background: transparent;
        border: none;
    """)

    lbl_desc = QLabel(descricao)
    lbl_desc.setStyleSheet(f"""
        color: {CORES['texto_suave']};
        font-size: 11px;
        background: transparent;
        border: none;
    """)

    coluna_texto.addWidget(lbl_titulo)
    coluna_texto.addWidget(lbl_desc)

    # Botão de executar — ainda sem função, aguarda aprovação para integrar DAO
    btn = QPushButton("Executar")
    btn.setObjectName("btn_acao")
    btn.setFixedWidth(90)
    btn.setStyleSheet(f"""
        QPushButton {{
            background-color: {cor};
            color: white;
            border: none;
            border-radius: 6px;
            padding: 7px 14px;
            font-size: 12px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            opacity: 0.85;
        }}
    """)

    layout.addWidget(indicador)
    layout.addLayout(coluna_texto)
    layout.addStretch()
    layout.addWidget(btn)

    return card


# ══════════════════════════════════════════════════════
# PÁGINA DE SEÇÃO — Clientes, Livros, etc.
# ══════════════════════════════════════════════════════
def criar_pagina_secao(titulo: str, subtitulo: str, acoes: list, cor: str) -> QWidget:
    """
    titulo    — nome da seção (ex: "Clientes")
    subtitulo — descrição curta
    acoes     — lista de tuplas (nome_acao, descricao)
    cor       — cor de destaque da seção
    """
    pagina = QWidget()

    layout_principal = QVBoxLayout(pagina)
    layout_principal.setContentsMargins(36, 30, 36, 30)
    layout_principal.setSpacing(0)

    # ── Cabeçalho ────────────────────────────────────
    cabecalho = QVBoxLayout()
    cabecalho.setSpacing(6)

    lbl_rotulo = QLabel(f"● {titulo.upper()}")
    lbl_rotulo.setStyleSheet(f"color: {cor}; font-size: 11px; font-weight: bold; letter-spacing: 2px;")

    lbl_titulo = QLabel(titulo)
    lbl_titulo.setStyleSheet(f"color: {CORES['texto']}; font-size: 28px; font-weight: bold;")

    lbl_sub = QLabel(subtitulo)
    lbl_sub.setStyleSheet(f"color: {CORES['texto_suave']}; font-size: 13px;")

    cabecalho.addWidget(lbl_rotulo)
    cabecalho.addWidget(lbl_titulo)
    cabecalho.addWidget(lbl_sub)
    layout_principal.addLayout(cabecalho)

    layout_principal.addSpacing(20)
    sep = QFrame()
    sep.setObjectName("separador")
    sep.setFrameShape(QFrame.HLine)
    layout_principal.addWidget(sep)
    layout_principal.addSpacing(20)

    # ── Área rolável com os cards de ação ───────────
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    container = QWidget()
    container.setStyleSheet("background: transparent;")
    col_acoes = QVBoxLayout(container)
    col_acoes.setSpacing(12)
    col_acoes.setContentsMargins(0, 0, 0, 0)

    for nome_acao, desc_acao in acoes:
        card = criar_card_acao(nome_acao, desc_acao, cor)
        col_acoes.addWidget(card)

    col_acoes.addStretch()
    scroll.setWidget(container)
    layout_principal.addWidget(scroll)

    return pagina


# ══════════════════════════════════════════════════════
# NAVEGAÇÃO DO MENU LATERAL
# ══════════════════════════════════════════════════════
def marcar_ativo(indice: int):
    """Desmarca todos os botões do menu e marca apenas o do índice recebido."""
    for i, btn in enumerate(botoes_menu):
        btn.setChecked(i == indice)


def navegar_para(indice: int):
    """Muda a página exibida no QStackedWidget e atualiza o botão ativo do menu."""
    paginas.setCurrentIndex(indice)
    marcar_ativo(indice)


# ══════════════════════════════════════════════════════
# MENU LATERAL FIXO (sidebar)
# ══════════════════════════════════════════════════════
def criar_menu_lateral() -> QFrame:
    global botoes_menu

    menu = QFrame()
    menu.setFixedWidth(220)
    menu.setStyleSheet(f"""
        QFrame {{
            background-color: {CORES['painel']};
            border-right: 1px solid {CORES['borda']};
        }}
    """)

    layout = QVBoxLayout(menu)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    # ── Logo / Título ────────────────────────────────
    header = QWidget()
    header.setFixedHeight(80)
    header.setStyleSheet(f"background-color: {CORES['painel']};")

    h_layout = QVBoxLayout(header)
    h_layout.setContentsMargins(20, 16, 20, 16)

    lbl_logo = QLabel("📚 Biblioteca")
    lbl_logo.setStyleSheet(f"color: {CORES['primaria']}; font-size: 18px; font-weight: bold;")

    lbl_versao = QLabel("v1.0 — Interface")
    lbl_versao.setStyleSheet(f"color: {CORES['texto_suave']}; font-size: 10px;")

    h_layout.addWidget(lbl_logo)
    h_layout.addWidget(lbl_versao)
    layout.addWidget(header)

    sep = QFrame()
    sep.setObjectName("separador")
    sep.setFrameShape(QFrame.HLine)
    sep.setStyleSheet(f"background-color: {CORES['borda']}; max-height: 1px;")
    layout.addWidget(sep)
    layout.addSpacing(8)

    # ── Itens de navegação ────────────────────────────
    itens_menu = [
        ("👤", "Clientes",      0),
        ("🧑‍💼", "Funcionários", 1),
        ("📖", "Livros",        2),
        ("📍", "Endereços",     3),
        ("📞", "Telefones",     4),
    ]

    botoes_menu = []

    for icone, rotulo, indice in itens_menu:
        btn = QPushButton(f"  {icone}  {rotulo}")
        btn.setObjectName("btn_menu")
        btn.setCheckable(True)
        btn.setFixedHeight(48)
        btn.clicked.connect(lambda checked, i=indice: navegar_para(i))

        botoes_menu.append(btn)
        layout.addWidget(btn)

    botoes_menu[0].setChecked(True)

    layout.addStretch()

    rodape = QLabel("SENAC-SP · Projeto Escola")
    rodape.setStyleSheet(f"color: {CORES['texto_suave']}; font-size: 10px; padding: 16px;")
    rodape.setAlignment(Qt.AlignCenter)
    layout.addWidget(rodape)

    return menu


# ══════════════════════════════════════════════════════
# DEFINIÇÃO DAS SEÇÕES E SUAS AÇÕES
# ══════════════════════════════════════════════════════
def montar_secoes() -> list:
    """
    Estrutura: (título, subtítulo, [(ação, descrição), ...], cor)
    NOTA: Os botões "Executar" ainda não chamam os DAOs.
          Integração pendente de aprovação.
    """
    return [
        (
            "Clientes",
            "Gerencie o cadastro de clientes da biblioteca",
            [
                ("Buscar por ID",           "Localiza um cliente pelo seu ID"),
                ("Buscar por Nome",         "Pesquisa clientes pelo nome"),
                ("Buscar por Email",        "Pesquisa pelo endereço de e-mail"),
                ("Buscar por CPF",          "Localiza pelo CPF"),
                ("Buscar por Nascimento",   "Filtra por data de nascimento"),
                ("Listar Todos",            "Exibe todos os clientes cadastrados"),
                ("Atualizar Status",        "Ativa ou bloqueia um cliente"),
                ("Atualizar Email e Senha", "Altera credenciais de acesso"),
                ("Atualizar Senha",         "Redefine apenas a senha"),
                ("Excluir Cliente",         "Remove permanentemente um cliente"),
            ],
            CORES["primaria"],
        ),
        (
            "Funcionários",
            "Gerencie a equipe da biblioteca",
            [
                ("Buscar por ID",         "Localiza um funcionário pelo ID"),
                ("Buscar por Nome",       "Pesquisa pelo nome"),
                ("Buscar por Email",      "Pesquisa pelo e-mail"),
                ("Buscar por CPF",        "Localiza pelo CPF"),
                ("Buscar por Cargo",      "Filtra funcionários por cargo"),
                ("Buscar por Nascimento", "Filtra por data de nascimento"),
                ("Listar Todos",          "Exibe todos os funcionários"),
                ("Dar Aumento",           "Atualiza o salário de um funcionário"),
                ("Promover",              "Atualiza cargo e salário"),
                ("Atualizar Email",       "Altera o e-mail do funcionário"),
                ("Atualizar Senha",       "Redefine a senha"),
                ("Excluir Funcionário",   "Remove permanentemente um funcionário"),
            ],
            CORES["sucesso"],
        ),
        (
            "Livros",
            "Controle o acervo e empréstimos",
            [
                ("Listar Todos",          "Exibe todo o acervo"),
                ("Verificar por Título",  "Busca por título ou trecho"),
                ("Verificar por ID",      "Busca direta pelo ID"),
                ("Pesquisar por Autor",   "Filtra pelo autor"),
                ("Pesquisar por Editora", "Filtra pela editora"),
                ("Pesquisar por Gênero",  "Filtra por gênero literário"),
                ("Pesquisar por Ano",     "Filtra pelo ano de publicação"),
                ("Emprestar Livro",       "Registra um novo empréstimo"),
                ("Devolver Livro",        "Registra a devolução"),
                ("Atualizar Quantidade",  "Ajusta o estoque do livro"),
                ("Excluir Livro",         "Remove um livro do acervo"),
            ],
            CORES["alerta"],
        ),
        (
            "Endereços",
            "Consulte e gerencie endereços cadastrados",
            [
                ("Listar de um Usuário",     "Endereços vinculados a um usuário"),
                ("Verificar CEP",            "Busca por CEP"),
                ("Verificar por Bairro",     "Filtra pelo bairro"),
                ("Verificar por Logradouro", "Filtra pelo logradouro"),
                ("Verificar por UF",         "Filtra pelo estado"),
                ("Verificar por Cidade",     "Filtra pela cidade"),
                ("Atualizar Endereço",       "Edita os dados de endereço"),
                ("Excluir Endereço",         "Remove um endereço cadastrado"),
            ],
            CORES["secundaria"],
        ),
        (
            "Telefones",
            "Gerencie os contatos telefônicos",
            [
                ("Buscar por Número",  "Localiza pelo número"),
                ("Buscar por Nome",    "Pesquisa pelo nome do titular"),
                ("Buscar por Tipo",    "Filtra por celular, fixo etc."),
                ("Buscar por Status",  "Filtra por status do número"),
                ("Atualizar Telefone", "Altera número e tipo"),
                ("Atualizar Status",   "Ativa ou desativa o número"),
                ("Excluir Telefone",   "Remove um contato"),
                ("Cadastrar Número",   "Adiciona novo contato"),
            ],
            "#43A8D9",   # azul-ciano para telefones
        ),
    ]


# ══════════════════════════════════════════════════════
# CONSTRUÇÃO DA JANELA PRINCIPAL
# ══════════════════════════════════════════════════════
def construir_janela():
    global janela, paginas

    janela = QMainWindow()
    janela.setWindowTitle("Sistema de Biblioteca")
    janela.setMinimumSize(900, 600)
    janela.resize(1100, 680)
    janela.setStyleSheet(ESTILO_GLOBAL)

    central = QWidget()
    janela.setCentralWidget(central)

    layout_raiz = QHBoxLayout(central)
    layout_raiz.setContentsMargins(0, 0, 0, 0)
    layout_raiz.setSpacing(0)

    # ── Páginas (uma por seção) ──────────────────────
    paginas = QStackedWidget()
    for titulo, sub, acoes, cor in montar_secoes():
        pagina = criar_pagina_secao(titulo, sub, acoes, cor)
        paginas.addWidget(pagina)

    # ── Menu lateral ──────────────────────────────────
    menu = criar_menu_lateral()

    layout_raiz.addWidget(menu)
    layout_raiz.addWidget(paginas)


# ══════════════════════════════════════════════════════
# PONTO DE ENTRADA
# ══════════════════════════════════════════════════════
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    construir_janela()
    janela.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()