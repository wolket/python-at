from src.base_page import BasePage
from src.components.grid.header import Header
from src.components.grid.pager import Pager
from src.components.grid.table import Table
from src.components.grid.tool_bar import ToolBar


class Grid(BasePage):
    def __init__(self, driver, locator, open_el=None):
        super().__init__(driver)

        grid = self._find_element(locator)

        self.header = Header(driver, grid)
        self.table = Table(driver, grid, self.header, open_el)

        #self.pager = Pager(driver, grid)
        #self.toolbar = ToolBar(driver, grid)
