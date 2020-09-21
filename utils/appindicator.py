
import gi

gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import AppIndicator3


class AppIndicator(object):
	# We can’t remove indicators, as far as I know,
	# so we recycle them. The application with most menu
	# that I‘ve seen is GIMP and LibreOofice with 11
	indicatorIds = []
	indicatorPool = []

	icons = [
		'folder-new', 'edit-cut', 'edit-select-all',
		'format-justify-left', 'media-playback-start', 'go-jump',
		'list-add', 'preferences-system', 'document-properties',
		'help-about', 'system-search'
	]

	def __init__(self, menus):
		super(AppIndicator, self).__init__()
		self.indicators = []
		self.icon_idx = 0

		for idx in range(len(menus)):
			menu = menus[idx]['menu']
			label = str(menus[idx]['label']).replace('_', '')
			if idx >= len(self.indicatorPool):
				indicator = self._create_indicator()

			indicator = self.indicatorPool[idx]
			print(f'{label=}')
			indicator.set_title(label + '-fildem')
			indicator.set_menu(menu)
			indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

	def _create_indicator(self):
		# Random id
		indicator_id = self.icons[self.icon_idx] + '-fildem'
		indicator = AppIndicator3.Indicator.new(indicator_id, self.icons[self.icon_idx], AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
		self.icon_idx += 1
		self.indicatorPool.append(indicator)
		self.indicatorIds.append(indicator_id)

	def hide_all(self):
		for indicator in self.indicatorPool:
			indicator.set_status(AppIndicator3.IndicatorStatus.PASSIVE)
			indicator.set_menu(Gtk.Menu())