import auth


# set up users
# set up permissions for certain actions
auth.authenticator.add_user('jordan', 'jpassword')
auth.authorizor.add_permission('disconnect campaign')
auth.authorizor.add_permission('reconnect campaign')
auth.authorizor.permit_user('disconnect campaign', 'jordan')
# hard code a few fake campaign IDs
campaign_ids_global = {
        1: 'disconnected',
        2: 'connected',
        3: 'connected', 
        4: 'connected'
        }
# write an editor to perform some CN related tasks
# have exceptions for campaigns IDs that don't exist
    # handle them


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            'login': self.login,
            'logout': self.logout,
            'dc': self.disconnect_campaigns,
            'quit': self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('Username: ')
            password = input('Password: ')
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print('Username does not exist')
            except auth.InvalidPassword:
                print('Invalid password')
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print(f'{e.username} is not logged in')
            return False
        except auth.NotPermittedError as e:
            print(f'{e.username} can not {permission}')
            return False
        else:
            return True

    def logout(self):
        self.username = False

    def disconnect_campaigns(self, campaign_ids):
        if self.is_permitted('disconnect campaign'):
            for campaign_id in campaign_ids:
                try: 
                    selected_campaign = campaign_ids_global[int(campaign_id)] 
                    campaign_ids_global[campaign_id] = 'disconnected'
                except KeyError:
                    print(f'{campaign_id} does not exist')
                else:
                    print(f'{campaign_id} -> {campaign_ids_global[campaign_id]}')
    
    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            while True:
                print('=' * 25)
                print("Please enter a command:\n" \
                "\tlogin\tLogin\n" \
                "\tquit\tQuit")
                answer = input('Enter a command: ').lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print(f'{answer} is not a valid option')
                else:
                    func()
                if self.username:
                    while True:
                        print('=' * 25)
                        print(f'Logged in as {self.username}')
                        print("Please enter a command:\n" \
                        "\tdc\tDisconnect campaigns\n" \
                        "\tlogout\tLogout")
                        answer = input('Enter a command: ')
                        try:
                            func = self.menu_map[answer]
                        except KeyError:
                            print(f'{answer} is not a valid option')
                        else:
                            if answer == 'logout':
                                func()
                                break
                            elif 'dc' in answer:
                                answer2 = input("enter the campaign you " \
                                                "would like to disconnect: ")
                                func(answer2.split(','))
                            else:
                                func()
        finally:
            print('Thanks, bye!!')


Editor().menu()
