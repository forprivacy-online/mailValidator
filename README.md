# 📬✅ mailValidator

[![US](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/us.png "Canada") English](/readme/en.md) -
[![Spain](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/es.png "Spain") Español](/readme/es.md) -
[![France](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/fr.png "France") Français](/readme/fr.md) -
[![Germany](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/de.png "Germany") Deutschland](/readme/de.md) -
[![China](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/cn.png "China") 中国](/readme/cn.md) -
[![India](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/in.png "China") हिंदी](/readme/in.md) -
[![Korea](https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/16/country-4x3/kr.png "Korea") 한국어](/readme/kr.md)

<br>

**mailValidator** es un paquete de Python para la verificación de direcciones de correo electrónico, que implementa varias validaciones para confirmar la validez de una dirección de correo. Si todas las validaciones fallan, el paquete utiliza **Abstract API** como último recurso.

<br>

## 🔍 Funcionalidades

1. **Validación de formato**: Verifica que la dirección de correo electrónico tenga un formato adecuado.
2. **Validación de registros MX**: Comprueba si el dominio del correo tiene registros MX válidos en el DNS.
3. **Verificación del servidor SMTP**: Verifica si el servidor SMTP del dominio está en funcionamiento.
4. **Validación de buzón de correo**: Intenta conectarse al servidor SMTP para verificar la existencia del buzón de correo.
5. **Validación con Abstract API** (opcional): Si todas las validaciones anteriores fallan, realiza una verificación final utilizando [Abstract API](https://www.abstractapi.com), que proporciona datos adicionales sobre la "entregabilidad" del correo electrónico.

<br>

## 🚀 Instalación

1. Clona el repositorio o descarga los archivos del proyecto.

```bash
git clone https://github.com/forprivacy-online/mailValidator.git
```

3. Instala las dependencias necesarias:

```bash
pip install dnspython requests
```

<br>

## 📄 Uso

Para comenzar a usar **mailValidator**, importa la clase `EmailVerifier` y llama al método `verify` con la dirección de correo electrónico que deseas verificar. 

**Nota**: Debes reemplazar `TU_CLAVE_DE_API` en el archivo `verifier.py` con tu clave de API de Abstract API para la verificación adicional.

```python
from email_verifier.verifier import EmailVerifier

email = "example@example.com"
is_valid, message = EmailVerifier.verify(email)
print(f"Valid: {is_valid}, Message: {message}")
```

### Ejemplo de salida

```bash
Valid: True, Message: Email is valid
```

<br>

## 📚 Funciones principales

- **`validate_format(email)`**: Verifica que el correo electrónico tenga un formato correcto.
- **`validate_mx_records(domain)`**: Comprueba si el dominio del correo tiene registros MX válidos.
- **`validate_smtp_server(domain)`**: Verifica si el servidor SMTP del dominio está en funcionamiento.
- **`validate_mailbox(email)`**: Intenta conectar con el servidor SMTP para verificar la existencia del buzón de correo.
- **`validate_with_abstract_api(email)`**: Realiza una verificación adicional con Abstract API si todas las anteriores validaciones fallan.

<br>

## 📝 Licencia

Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT).
