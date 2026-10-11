
from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"id": 1, "name": "Indoor Plant", "price": 99},
    {"id": 2, "name": "Gardening Kit", "price": 199},
    {"id": 3, "name": "Plant Pot", "price": 79},
]

HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1">

    <title>GREEN MART | Online Store</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f1f7f1;
            color: #203528;
        }

        header {
            background: #17452c;
            color: white;
            text-align: center;
            padding: 25px 10px;
        }

        header h1 {
            margin: 0;
            font-size: 32px;
        }

        main {
            max-width: 900px;
            margin: 30px auto;
            padding: 15px;
        }

        .products {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(190px, 1fr));
            gap: 18px;
        }

        .card {
            background: white;
            padding: 22px;
            border-radius: 12px;
            box-shadow: 0 3px 10px #0001;
        }

        .price {
            color: #168044;
            font-size: 22px;
            font-weight: bold;
        }

        .btn {
            display: inline-block;
            background: #21834b;
            color: white;
            padding: 10px 15px;
            border-radius: 6px;
            text-decoration: none;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: #526557;
        }
    </style>
</head>

<body>
    <header>
        <h1>🌱 GREEN MART</h1>
        <p>आपकी अपनी ऑनलाइन दुकान</p>
    </header>

    <main>
        <h2>हमारे प्रोडक्ट</h2>
        <p>पौधों और गार्डनिंग की दुनिया में आपका स्वागत है।</p>

        <div class="products">
            {% for product in products %}
                <div class="card">
                    <h3>{{ product.name }}</h3>
                    <p class="price">₹{{ product.price }}</p>
                    <p>अच्छी क्वालिटी का प्रोडक्ट।</p>
                    <a class="btn" href="#contact">
                        जानकारी लें
                    </a>
                </div>
            {% endfor %}
        </div>

        <section id="contact">
            <h2>हमसे संपर्क करें</h2>
            <p>ऑर्डर की सुविधा अगले चरण में जोड़ेंगे।</p>
        </section>
    </main>

    <footer>
        © 2026 GREEN MART | Made with Python
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)
