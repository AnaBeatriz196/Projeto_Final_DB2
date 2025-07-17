from app import create_app

# Cria a instância da aplicação com a configuração padrão
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
