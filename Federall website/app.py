import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_loadstring', methods=['POST'])
def generate_loadstring():
    try:
        data = request.json
        script = data.get('script')
        if not script:
            return jsonify({"error": "No script provided"}), 400

        # Generate the loadstring
        custom_loadstring = f'loadstring("federall {script}")()'

        # Return the hidden version (simulate obfuscation)
        return jsonify({"loadstring": custom_loadstring}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
