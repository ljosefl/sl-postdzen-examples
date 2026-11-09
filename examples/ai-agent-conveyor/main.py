from flask import Flask, jsonify
import mysql.connector
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)

# AI Agent setup
llm = OpenAI(temperature=0)
prompt = PromptTemplate(
    input_variables=["user_id"],
    template="Get user information with ID: {user_id}"
)
chain = LLMChain(llm=llm, prompt=prompt)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return jsonify({"user_id": result[0], "name": result[1], "email": result[2]})
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_api', methods=['POST'])
def generate_api():
    try:
        user_id = int(request.form['user_id'])
        response = chain.run(user_id)
        return jsonify({"api_response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)