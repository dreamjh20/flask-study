from flask import Flask
Moon = Flask(__name__)

@Moon.route('/message/<int:message_id>')
def get_message(message_id):
    print("--%d--\n" %message_id)
    return 'message_id: %d' %message_id

if __name__ == '__main__':
    Moon.run()