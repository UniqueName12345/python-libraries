import fancyterminal

ft = fancyterminal.FT_Terminal()
ft.version()

speak = ft.meta_input('What do you want to say? ')
ft.success_input('You said: ' + speak)