'''
A very basic Flask app to control my markdown files
'''

from flask import Flask, request
import markdown

app = Flask(__name__)

@app.route('/tips/<tip>', methods = ['GET'])
@app.route('/')
def index(tip='tips.md'):
	if not tip.startswith('tips'):
		tip = 'tips/{0}'.format(tip)
	print tip
	try:
		with open(tip, 'r') as f:
			md = f.read()
		return '''
		<html>
			<body>
			{0}
			</body>
		</html>
		'''.format(markdown.markdown(md, ['fenced_code']))
	except IOError:
		return ''

if __name__ == '__main__':
	app.run(debug=True)
