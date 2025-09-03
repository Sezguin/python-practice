from dataclasses import dataclass

@dataclass
class Item:
  item_name: str
  item_price: int
  item_type: str
  item_in_stock: bool


class ItemClass():
  def __init__(self):
    self._item_list: list[Item] = []

  def get_list_of_items(self):
    return self._item_list

  def get_single_item(self, item_name):
    return (next(item for item in self._item_list if item_name == item.name), None)

  def create_an_item(self, item_name: str, item_price: int, item_type: str, item_in_stock: bool) -> Item:
    self.validate_item_data()