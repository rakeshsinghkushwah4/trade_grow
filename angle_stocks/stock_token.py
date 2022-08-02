from smartapi import SmartConnect

class AngleToken:

  def __init__(self, token, client_id, password):
    self.session = SmartConnect(api_key=token)
    token = self.session.generateSession(client_id, password)
    self.refresh_token = token['data']['refreshToken']
  
  def get_session(self):
    session = self.session
    return session

  def get_token(self):
    token = self.refresh_token
    return token
