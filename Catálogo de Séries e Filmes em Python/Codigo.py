import sqlite3
import tkinter as tk
from tkinter import messagebox, Listbox
import unicodedata

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto

def normalizar_tipo(texto):
    texto = normalizar_texto(texto) 
    if texto in ['filme', 'serie']: 
        return 'Filme' if texto == 'filme' else 'Série'
    else:
        raise Exception("Tipo inválido! Digite 'Filme' ou 'Série'.")

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('catalogo.db')
        self.create_tables() 

    def create_tables(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS genero (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS serie_filme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                tipo TEXT CHECK(tipo IN ('Filme', 'Série')),
                ano_lancamento INTEGER,
                id_genero INTEGER,
                FOREIGN KEY(id_genero) REFERENCES genero(id)
            )
        ''')
        self.conexao.commit()

    def inserir_genero(self, nome):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT OR IGNORE INTO genero (nome) VALUES (?)", (nome,))
        self.conexao.commit()

    def listar_generos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM genero")
        return cursor.fetchall()

    def buscar_genero_por_nome(self, nome):
        nome_normalizado = normalizar_texto(nome)
        cursor = self.conexao.cursor()
        cursor.execute("SELECT id, nome FROM genero")
        for id_genero, nome_genero in cursor.fetchall():
            if normalizar_texto(nome_genero) == nome_normalizado:
                return id_genero  
        return None  

    def inserir_serie_filme(self, titulo, tipo, ano, id_genero):
        cursor = self.conexao.cursor()
        cursor.execute("""
            INSERT INTO serie_filme (titulo, tipo, ano_lancamento, id_genero)
            VALUES (?, ?, ?, ?)
        """, (titulo, tipo, ano, id_genero))
        self.conexao.commit()

    def listar_series_filmes(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            SELECT sf.id, sf.titulo, sf.tipo, sf.ano_lancamento, g.nome
            FROM serie_filme sf
            JOIN genero g ON sf.id_genero = g.id
        """)
        return cursor.fetchall()

    def atualizar_serie_filme(self, id, titulo, tipo, ano, id_genero):
        cursor = self.conexao.cursor()
        cursor.execute("""
            UPDATE serie_filme
            SET titulo = ?, tipo = ?, ano_lancamento = ?, id_genero = ?
            WHERE id = ?
        """, (titulo, tipo, ano, id_genero, id))
        self.conexao.commit()

    def excluir_serie_filme(self, id):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM serie_filme WHERE id = ?", (id,))
        self.conexao.commit()

class Aplicacao:
    def __init__(self, master):
        self.master = master
        master.title("Catálogo de Séries e Filmes")  # Título da janela
        self.banco = Banco()  # Instancia a classe banco para usar

        tk.Label(master, text="ID (para atualizar/excluir):").grid(row=0, column=0)
        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=0, column=1)

        tk.Label(master, text="Título:").grid(row=1, column=0)
        self.titulo_entry = tk.Entry(master)
        self.titulo_entry.grid(row=1, column=1)

        tk.Label(master, text="Tipo (Filme/Série):").grid(row=2, column=0)
        self.tipo_entry = tk.Entry(master)
        self.tipo_entry.grid(row=2, column=1)

        tk.Label(master, text="Ano de Lançamento:").grid(row=3, column=0)
        self.ano_entry = tk.Entry(master)
        self.ano_entry.grid(row=3, column=1)

        tk.Label(master, text="Gênero (Nome):").grid(row=4, column=0)
        self.genero_entry = tk.Entry(master)
        self.genero_entry.grid(row=4, column=1)

        tk.Button(master, text="Inserir", command=self.inserir).grid(row=5, column=0)
        tk.Button(master, text="Atualizar", command=self.atualizar).grid(row=5, column=1)
        tk.Button(master, text="Excluir", command=self.excluir).grid(row=6, column=0)
        tk.Button(master, text="Listar", command=self.listar).grid(row=6, column=1)
        tk.Button(master, text="Listar Gêneros", command=self.listar_generos).grid(row=7, column=0, columnspan=2)

        self.listbox = Listbox(master, width=80)
        self.listbox.grid(row=8, column=0, columnspan=2)

    def get_genero_id(self, nome_genero):
        id_genero = self.banco.buscar_genero_por_nome(nome_genero)
        if id_genero is None:
            raise Exception(f"Gênero '{nome_genero}' não encontrado! Clique em 'Listar Gêneros' para ver os disponíveis.")
        return id_genero

    def inserir(self):
        try:
            titulo = self.titulo_entry.get()
            tipo = normalizar_tipo(self.tipo_entry.get())
            ano = int(self.ano_entry.get())
            genero_nome = self.genero_entry.get()
            id_genero = self.get_genero_id(genero_nome) 
            self.banco.inserir_serie_filme(titulo, tipo, ano, id_genero) 
            messagebox.showinfo("Sucesso", "Registro inserido com sucesso!")
            self.listar()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao inserir: {e}")

    def atualizar(self):
        try:
            id = int(self.id_entry.get()) 
            titulo = self.titulo_entry.get()
            tipo = normalizar_tipo(self.tipo_entry.get())
            ano = int(self.ano_entry.get())
            genero_nome = self.genero_entry.get()
            id_genero = self.get_genero_id(genero_nome)
            self.banco.atualizar_serie_filme(id, titulo, tipo, ano, id_genero) 
            messagebox.showinfo("Sucesso", "Registro atualizado!")
            self.listar()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar: {e}")

    def excluir(self):
        try:
            id = int(self.id_entry.get())
            self.banco.excluir_serie_filme(id)
            messagebox.showinfo("Sucesso", "Registro excluído!")
            self.listar()
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao excluir: {e}")

    def listar(self):
        self.listbox.delete(0, tk.END) 
        for row in self.banco.listar_series_filmes():
            self.listbox.insert(tk.END, f"ID: {row[0]} | Título: {row[1]} | Tipo: {row[2]} | Ano: {row[3]} | Gênero: {row[4]}")

    def listar_generos(self):
        self.listbox.delete(0, tk.END)
        generos = self.banco.listar_generos()
        if not generos:
            self.listbox.insert(tk.END, "Nenhum gênero cadastrado ainda.")
        for row in generos:
            self.listbox.insert(tk.END, f"ID: {row[0]} | Gênero: {row[1]}")

    def limpar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)
        self.ano_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)

def inserir_generos_iniciais():
    banco = Banco()
    generos = ['Ação', 'Comédia', 'Drama', 'Terror', 'Animação']
    for genero in generos:
        banco.inserir_genero(genero)

if __name__ == "__main__":
    inserir_generos_iniciais() 
    root = tk.Tk() 
    app = Aplicacao(root)
    root.mainloop()
