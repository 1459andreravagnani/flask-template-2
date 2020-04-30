from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    pokemons = [
        ['Guaraná  R$: 4.50', 'https://savegnago.vteximg.com.br/arquivos/ids/288962-1000-1000/REFRIGERANTE-ANTARCTICA-350ML-LATA-GUARA.jpg?v=636639069900630000'],
     
        ['Pizza R$: 2.50', 'https://img.stpu.com.br/?img=https://s3.amazonaws.com/pu-mgr/default/a0R0f000010xA7GEAU/5c489cd8e4b0842c9b1b6c10.jpg&w=710&h=462'],
     
        ['Suco R$: 24.90', 'https://casafiesta.fbitsstatic.net/img/p/suco-de-laranja-integral-prats-900ml-66809/233677.jpg?w=800&h=800&v=no-change'],
   
        ['Lanche R$: 18.50', 'https://lh3.googleusercontent.com/proxy/s3xKllKT9sIKGTNuSo1I2FPE_ERAC4N32vN2kh6DA4vIv3Qj2iqGV5ecZQ1bOrQzzgk9UrhNPAbAc3juHtoGC_pK5p_iocavf303ik-IEXW8uVV9rk7_FTK9']
    ]
    return render_template(
        'index.html',
        titulo='Pokedex',
        pokemons=pokemons
    )
 
if __name__ == '__main__':
    app.run()

    
