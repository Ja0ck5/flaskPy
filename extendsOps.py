# coding=utf-8
class Cat:
    color = 'black'

    legs = 4

    weight = 6

    def __init__(self):
        print '------- parent cat ----------'

    def __del__(self):
        print '========= parent cat =========='

    def say(self):
        print 'mew mew~'

    def catch(self):
        print 'catch mouse'


class Bosi(Cat):
    def __init__(self):
        Cat.__init__(self)
        print '------- child bosi ----------'

    def __del__(self):
        print '========= child bosi =========='

    def bosiRun(self):
        print 'I am a bosi cat.I am running...'


class BastardCat(Cat, Bosi):
    def bastardCatSay(self):
        print 'u bastard.'


# ------- child bosi ----------
# ------- parent cat ----------
# ========= parent cat ==========
# ========= child bosi ==========
# bosi = Bosi()
# parentCat = Cat()
# bosi.say()
# bosi.bosiRun()
# parentCat.say()

# ------- parent cat ----------
# ------- child bosi ----------
# ========= parent cat ==========
# ========= child bosi ==========

# ------- parent cat ----------
# ------- child bosi ----------
# ------- parent cat ----------
# u bastard.
# ========= parent cat ==========
# ========= parent cat ==========
# ========= child bosi ==========

# parentCat = Cat()
# bosi = Bosi()

# bc = BastardCat()
# bc.bastardCatSay()


# ------- parent cat ----------
# u bastard.
# ========= parent cat ==========


bc = BastardCat()
bc.bastardCatSay()
