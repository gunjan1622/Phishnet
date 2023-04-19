from pywinauto import Application
# extract the url from the address bar and return it

class AddressBar:
    @staticmethod
    def get_url()->str:
        app = Application(backend='uia')
        app.connect(title_re=".*Chrome.*")
        element_name="Address and search bar"
        dlg = app.top_window()
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
        return url
    
    @staticmethod
    def set_url(url:str)->str:
        app = Application(backend='uia')
        app.connect(title_re=".*Chrome.*")
        element_name="Address and search bar"
        dlg = app.top_window()
        dlg.child_window(title=element_name, control_type="Edit").set_edit_text(url)
        return url

    @staticmethod
    def redirect_url(url:str)->str:
        app = Application(backend='uia')
        app.connect(title_re=".*Chrome.*")
        element_name="Address and search bar"
        dlg = app.top_window()
        dlg.child_window(title=element_name, control_type="Edit").set_edit_text(url)
        dlg.child_window(title=element_name, control_type="Edit").type_keys("{ENTER}")
        return url