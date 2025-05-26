from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24) # Necessário para flash messages

# Configuração do Flask-Mail (USUÁRIO PRECISA ALTERAR COM DADOS REAIS E CONFIGURAR NA VERCEL)
# Recomenda-se usar variáveis de ambiente para todas estas configurações em produção
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.example.com")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS", "True").lower() == "true"
app.config["MAIL_USE_SSL"] = os.getenv("MAIL_USE_SSL", "False").lower() == "true"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME", "seu_email@example.com")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD", "sua_senha_de_email")
mail_sender_name = os.getenv("MAIL_DEFAULT_SENDER_NAME", "Adote um Amigo")
mail_sender_email = os.getenv("MAIL_DEFAULT_SENDER_EMAIL", "contato@adoteumamigo.com")
app.config["MAIL_DEFAULT_SENDER"] = (mail_sender_name, mail_sender_email)

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "edvaniesb@gmail.com") # E-mail do administrador para receber notificações

mail = Mail(app)

# Dados mockados para a busca (substituir por banco de dados ou outra fonte de dados real)
animais_db = [
    {"id": 1, "nome": "Rex", "especie": "Cachorro", "raca": "Labrador", "idade": "2 anos", "descricao": "Amigável e brincalhão, ótimo com crianças.", "imagem": "images/labrador.jpg"},
    {"id": 2, "nome": "Mimi", "especie": "Gato", "raca": "Siamês", "idade": "1 ano", "descricao": "Calma e carinhosa, adora um colo.", "imagem": "images/siames.jpg"},
    {"id": 3, "nome": "Bolinha", "especie": "Cachorro", "raca": "Poodle", "idade": "3 anos", "descricao": "Pequeno e enérgico, precisa de espaço para correr.", "imagem": "images/Poodle.jpg"},
    {"id": 4, "nome": "Tom", "especie": "Gato", "raca": "Persa", "idade": "5 anos", "descricao": "Muito tranquilo e independente.", "imagem": "images/persa.jpg"},
    {"id": 5, "nome": "Max", "especie": "Cachorro", "raca": "Golden Retriever", "idade": "6 meses", "descricao": "Filhote adorável e cheio de energia.", "imagem": "images/golden.jpg"},
    { "id": 6,"nome": "Luna","especie": "Gato","raca": "Munchkin", "idade": "4 meses", "descricao": "Gata de pernas curtas, muito brincalhona, carinhosa e com aparência de filhote permanente.","imagem": "images/Munchkin.jpg"}

]

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}

@app.route("/")
def index():
    animais_para_galeria = animais_db[:3]
    return render_template("index.html", animais=animais_para_galeria)

@app.route("/subscribe_newsletter", methods=["POST"])
def subscribe_newsletter():
    if request.method == "POST":
        email_inscrito = request.form.get("email")
        if email_inscrito:
            try:
                assunto = "Inscrição na Newsletter Adote um Amigo Confirmada!"
                corpo_html = f"<p>Olá,</p><p>Obrigado por se inscrever na nossa newsletter com o e-mail: {email_inscrito}.</p><p>Você receberá novidades sobre nossos animais, eventos de adoção e dicas.</p><p>Atenciosamente,<br>Equipe Adote um Amigo</p>"
                assunto_admin = f"Nova Inscrição na Newsletter: {email_inscrito}"
                corpo_admin_html = f"<p>Nova inscrição na newsletter:</p><p>E-mail: {email_inscrito}</p>"

                msg_usuario = Message(subject=assunto, recipients=[email_inscrito], html=corpo_html)
                msg_admin = Message(subject=assunto_admin, recipients=[ADMIN_EMAIL], html=corpo_admin_html)
                
                # mail.send(msg_usuario)
                # mail.send(msg_admin)
                
                print(f"Simulando envio de e-mail de newsletter para: {email_inscrito}")
                print(f"Simulando envio de e-mail de newsletter para admin: {ADMIN_EMAIL} sobre {email_inscrito}")

                flash(f"Obrigado por se inscrever, {email_inscrito}! Um e-mail de confirmação foi enviado (simulado).", "success")
            except Exception as e:
                print(f"Erro ao tentar enviar e-mail de newsletter: {e}")
                flash("Ocorreu um erro ao processar sua inscrição na newsletter. Tente novamente mais tarde.", "danger")
        else:
            flash("Por favor, forneça um e-mail válido para a newsletter.", "warning")
    return redirect(url_for("index") + "#contato")

@app.route("/search")
def search():
    query = request.args.get("query", "").lower()
    resultados = []
    if query:
        for animal in animais_db:
            if (query in animal["nome"].lower() or 
                query in animal["especie"].lower() or 
                query in animal["raca"].lower() or 
                query in animal["descricao"].lower()):
                resultados.append(animal)
    
    if query:
        if resultados:
            flash(f"{len(resultados)} resultado(s) encontrado(s) para \'{query}\'.", "info")
        else:
            flash(f"Nenhum resultado encontrado para \'{query}\'.", "warning")
    
    return render_template("index.html", animais=animais_db[:3], search_results=resultados, query=query)

@app.route("/formulario-adocao", methods=["GET"])
def adoption_form_page():
    return render_template("formulario_adocao.html")

@app.route("/submit-adoption-form", methods=["POST"])
def submit_adoption_form():
    if request.method == "POST":
        nome_completo = request.form.get("nome_completo")
        email_solicitante = request.form.get("email")
        telefone = request.form.get("telefone")
        endereco_rua = request.form.get("endereco_rua")
        endereco_numero = request.form.get("endereco_numero")
        endereco_complemento = request.form.get("endereco_complemento")
        endereco_bairro = request.form.get("endereco_bairro")
        endereco_cidade = request.form.get("endereco_cidade")
        endereco_estado = request.form.get("endereco_estado")
        endereco_cep = request.form.get("endereco_cep")
        tipo_moradia = request.form.get("tipo_moradia")
        outros_animais = request.form.get("outros_animais")
        porque_adotar = request.form.get("porque_adotar")
        animal_interesse = request.form.get("animal_interesse")
        mensagem_adicional = request.form.get("mensagem_adicional")

        if not all([nome_completo, email_solicitante, telefone, endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado, endereco_cep, tipo_moradia, porque_adotar]):
            flash("Por favor, preencha todos os campos obrigatórios do formulário de adoção.", "danger")
            return redirect(url_for("adoption_form_page"))

        try:
            assunto_admin = f"Nova Solicitação de Adoção: {nome_completo}"
            corpo_html_admin = f"<h3>Nova Solicitação de Interesse em Adoção Recebida:</h3>"
            corpo_html_admin += f"<p><strong>Nome Completo:</strong> {nome_completo}</p>"
            corpo_html_admin += f"<p><strong>E-mail:</strong> {email_solicitante}</p>"
            corpo_html_admin += f"<p><strong>Telefone:</strong> {telefone}</p>"
            corpo_html_admin += f"<hr>"
            corpo_html_admin += f"<p><strong>Endereço:</strong> {endereco_rua}, Nº {endereco_numero} {endereco_complemento if endereco_complemento else ''}</p>"
            corpo_html_admin += f"<p><strong>Bairro:</strong> {endereco_bairro}</p>"
            corpo_html_admin += f"<p><strong>Cidade/Estado:</strong> {endereco_cidade}/{endereco_estado} - CEP: {endereco_cep}</p>"
            corpo_html_admin += f"<hr>"
            corpo_html_admin += f"<p><strong>Tipo de Moradia:</strong> {tipo_moradia}</p>"
            corpo_html_admin += f"<p><strong>Possui outros animais?</strong> {outros_animais if outros_animais else 'Não informado'}</p>"
            corpo_html_admin += f"<p><strong>Por que deseja adotar?</strong><br>{porque_adotar}</p>"
            corpo_html_admin += f"<p><strong>Animal de Interesse:</strong> {animal_interesse if animal_interesse else 'Não especificado'}</p>"
            corpo_html_admin += f"<p><strong>Mensagem Adicional:</strong><br>{mensagem_adicional if mensagem_adicional else 'Nenhuma'}</p>"
            
            msg_admin = Message(subject=assunto_admin, recipients=[ADMIN_EMAIL], html=corpo_html_admin)
            # mail.send(msg_admin)
            print(f"Simulando envio de e-mail de adoção para admin: {ADMIN_EMAIL} sobre {nome_completo}")

            assunto_solicitante = "Recebemos sua Solicitação de Adoção!"
            corpo_html_solicitante = f"<p>Olá {nome_completo},</p>"
            corpo_html_solicitante += f"<p>Recebemos sua solicitação de interesse em adoção. Agradecemos muito seu contato!</p>"
            corpo_html_solicitante += f"<p>Em breve, nossa equipe analisará seus dados e entrará em contato.</p>"
            corpo_html_solicitante += f"<p>Atenciosamente,<br>Equipe Adote um Amigo</p>"
            
            msg_solicitante = Message(subject=assunto_solicitante, recipients=[email_solicitante], html=corpo_html_solicitante)
            # mail.send(msg_solicitante)
            print(f"Simulando envio de e-mail de confirmação de adoção para: {email_solicitante}")

            flash("Sua solicitação de adoção foi enviada com sucesso! Entraremos em contato em breve.", "success")
            return redirect(url_for("index"))

        except Exception as e:
            print(f"Erro ao processar formulário de adoção: {e}")
            flash("Ocorreu um erro ao enviar sua solicitação. Tente novamente mais tarde.", "danger")
            return redirect(url_for("adoption_form_page"))

    return redirect(url_for("adoption_form_page"))

@app.route("/como-ajudar")
def como_ajudar_page():
    return render_template("como_ajudar.html")

@app.route("/resgate-gatinho")
def resgate_gatinho_page():
    return render_template("resgate_gatinho.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

