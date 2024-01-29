from app import app
import os

# Habilitar o modo de depuração
app.run(debug=True)

""" if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port) """