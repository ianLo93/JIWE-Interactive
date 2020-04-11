"""
User class for user info container.
"""
class User:

    users = set()
    user_online = {} # client-connection mapping

    @staticmethod
    def user_sign_up(username):
        if username in User.users:
            print("Error: username " + username + " already exists")
            return False
        else:
            User.user_online.add(username)
            return True

    @staticmethod
    def user_log_on(username, conn, addr):
        if username not in User.users:
            User.user_online[username] = (conn, addr)
            return True
        else:
            print("Error: user " + username + "hasn't signed up yet")
            return False

    @staticmethod
    def user_log_off(username):
        try:
            del User.user_online[username]
            return True
        except:
            print("Error: should not try to remove a non-exist user " + username)
            return False

    @staticmethod
    def online_check(username):
        # check the user online status every now and then
        pass

if __name__ == '__main__':
    pass
