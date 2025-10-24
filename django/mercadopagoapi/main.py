import mercadopago

sdk = mercadopago.SDK("TOKEN")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    "x-idempotency-key": "public_key"
}

payment_data = {
    "transaction_amount": 58.00,
    "description": "Payment for product",
    "installments": 1,
    "token": "card_token",
    "payer": {
        "email": "test_user_123@testuser.com",
        "identification": {
            "type": "CPF",
            "number": "19119119100"  # CPF de teste do sandbox. Troque se tiver outro válido.
        }
    },
    "capture": True,  # capture direto; remova se quiser default
    "payment_method_id": "master",  # pode omitir se o token já define a bandeira
    "external_reference": "MP0001",
    "notification_url": "https://www.suaurl.com/notificacoes/"
}

payment_response = sdk.payment().create(payment_data, request_options)
payment = payment_response["response"]

print(payment, '<<<')
