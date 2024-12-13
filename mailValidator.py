import re
import smtplib
import dns.resolver
import socket
import requests

# 1. Validar formato de correo electrónico
def validate_format(email):
    """
    Verifica que el correo electrónico tenga un formato correcto.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 2. Validar registros MX del dominio
def validate_mx_records(domain):
    """
    Comprueba si el dominio del correo tiene registros MX válidos.
    """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return False

# 3. Validar el servidor SMTP
def validate_smtp_server(domain):
    """
    Verifica si el servidor SMTP del dominio está en funcionamiento.
    """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = sorted(mx_records, key=lambda r: r.preference)[0]  # Prioriza el MX de menor preferencia
        smtp_server = str(mx_record.exchange).rstrip('.
')
        
        # Probar conexión con el servidor SMTP en el puerto 25
        with smtplib.SMTP(timeout=10) as server:
            server.connect(smtp_server, 25)
            return True
    except (dns.resolver.NoAnswer, dns.exception.Timeout, socket.error, smtplib.SMTPException):
        return False

# 4. Validar existencia del buzón de correo
def validate_mailbox(email):
    """
    Intenta conectar con el servidor SMTP para verificar la existencia del buzón de correo.
    """
    try:
        domain = email.split('@')[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = sorted(mx_records, key=lambda r: r.preference)[0]  # Prioriza el MX de menor preferencia
        smtp_server = str(mx_record.exchange).rstrip('.
')
        
        with smtplib.SMTP(timeout=10) as server:
            server.connect(smtp_server, 25)
            server.helo(socket.gethostname())  # Identificación del cliente SMTP
            server.mail('test@example.com')  # Remitente ficticio
            code, _ = server.rcpt(email)  # Intentar enviar al destinatario
            return code == 250  # Código 250 significa que el buzón es válido
    except (dns.resolver.NoAnswer, dns.exception.Timeout, socket.error, smtplib.SMTPException):
        return False

# 5. Validación con Abstract API
def validate_with_abstract_api(email, api_key):
    """
    Realiza una validación adicional con Abstract API.
    """
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={api_key}&email={email}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('deliverability') == 'DELIVERABLE'
    except requests.RequestException:
        return False

# Función principal para orquestar las validaciones
def validate_email(email, api_key):
    """
    Realiza todas las validaciones necesarias para un correo electrónico.
    """
    print(f"Validando: {email}\n")
    
    # 1. Validar formato
    if not validate_format(email):
        print("[Error] Formato de correo electrónico no válido.")
        return False
    print("[OK] Formato de correo válido.")
    
    # Extraer dominio
    domain = email.split('@')[1]
    
    # 2. Validar registros MX
    if not validate_mx_records(domain):
        print("[Error] No se encontraron registros MX para el dominio.")
        return False
    print("[OK] Registros MX encontrados.")
    
    # 3. Validar servidor SMTP
    if not validate_smtp_server(domain):
        print("[Error] No se pudo contactar con el servidor SMTP.")
        return False
    print("[OK] Servidor SMTP operativo.")
    
    # 4. Validar buzón de correo
    if not validate_mailbox(email):
        print("[Error] El buzón de correo no existe.")
        print("[INFO] Realizando validación con Abstract API...")
        if validate_with_abstract_api(email, api_key):
            print("[OK] Validación con Abstract API exitosa.")
            return True
        print("[Error] La validación con Abstract API también falló.")
        return False
    print("[OK] Buzón de correo verificado.")
    
    return True
