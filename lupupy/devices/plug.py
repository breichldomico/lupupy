"""Lupusec plug device."""

from lupupy.devices import LupusecDevice
import lupupy.constants as CONST


class LupusecPlug(LupusecDevice):
    """Class to add switch functionality."""

    def switch_on(self):
        """Turn the switch on."""
        success = self.set_status(CONST.STATUS_PLUG_ON_INT)

        if success:
            self._json_state['status'] = CONST.STATUS_PLUG_ON

        return success

    def switch_off(self):
        """Turn the switch off."""
        success = self.set_status(CONST.STATUS_PLUG_OFF_INT)

        if success:
            self._json_state['status'] = CONST.STATUS_PLUG_OFF

        return success

    @property
    def is_on(self):
        """
        Get switch state.

        Assume switch is on.
        """
        _LOGGER.info("Plug")
        return self.status not in (CONST.STATUS_PLUG_OFF, CONST.STATUS_OFFLINE, STATUS_POWER_OFF)

    @property
    def is_dimmable(self):
        """Device dimmable."""
        return False
