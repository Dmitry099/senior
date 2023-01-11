from abc import ABC, abstractmethod


class Director(ABC):

    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class FormBuilder(ABC):

    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass


class HTMLForm:
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return "<form>{}</form>".format("".join(self.field_list))


class HTMLFormBuilder(FormBuilder):

    def __init__(self):
        self.constructed_object = HTMLForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(
                field_dict['label'],
                field_dict['field_name'],
            )
        )

    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            '<label><br><input type="checkbox" id="{0}" value="{1}"> {2}<br>'.format(
                checkbox_dict['field_id'],
                checkbox_dict['value'],
                checkbox_dict['label']
            )
        )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(
                button_dict['text']
            )
        )


class FormDirector(Director):

    builder_types = {
        "text_field": "add_text_field",
        "checkbox": "add_checkbox",
        "button": "add_button"
    }

    def __init__(self):
        super().__init__()

    def construct(self, field_list):
        for field in field_list:
            getattr(
                self._builder, self.builder_types[field["field_type"]]
            )(field)


if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HTMLFormBuilder()
    director.set_builder(html_form_builder)
    field_list = [
        {
            "field_type": "text_field",
            "label": "Some label",
            "field_name": "Field one"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "Some label2"
        },
        {
            "field_type": "button",
            "text": "DONE"
        }
    ]
    director.construct(field_list)
    print(director.get_constructed_object())
