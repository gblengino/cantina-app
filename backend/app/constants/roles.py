class Roles:
    ADMIN = "admin"
    CASHIER = "cashier"
    INVENTORY_MANAGER = "inventory_manager"

    @classmethod
    def values(cls):
        return [
            cls.ADMIN,
            cls.CASHIER,
            cls.INVENTORY_MANAGER
        ]