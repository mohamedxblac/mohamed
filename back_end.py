from flask import Flask, request, jsonify
import cohere

app = Flask(__name__)

# إعداد العميل
co = cohere.ClientV2("EWrRoKsxtZ7J329VFwYZwuYQGbKR6EgAe6YJF1Ir")

@app.route('/chat', methods=['POST'])
def chat_with_cohere():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        # إرسال الرسالة إلى Cohere
        response = co.chat(
            model="command-r-plus",
            messages=[{"role": "user", "content": user_message}]
        )
        
        # استخراج النص من الاستجابة
        ai_response = response.message.content[0].text

        return jsonify({"message": ai_response}), 200

    except Exception as e:
        print("Error:", str(e))  # طباعة الخطأ للتصحيح
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
