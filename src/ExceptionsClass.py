class ZeroQuantityError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = (
            args[0]
            if args
            else "Товар с нулевым количеством не может быть добавлен в категорию."
        )

    def __str__(self):
        return self.message
