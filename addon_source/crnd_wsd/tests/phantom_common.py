from odoo.addons.generic_mixin.tests.common import WebTourCase

from odoo.addons.generic_mixin.tests.common import deactivate_records_for_model


class TestPhantomTour(WebTourCase):

    def setUp(self):
        super(TestPhantomTour, self).setUp()

        # Disable assets from uninstalled modules
        deactivate_records_for_model(self.env, 'ir.asset')

    def _test_phantom_tour(self, start_url, tour_name, **kw):
        """ Wrapper to run web tours
        """
        return self.run_js_tour(start_url, tour_name, **kw)

    def _test_phantom_tour_requests(self, start_url, tour_name, **kw):
        """ Same as _test_phantom_tour but returns list of requests
            generated by tour
        """
        requests_before = self.env['request.request'].search([])
        self._test_phantom_tour(start_url, tour_name, **kw)
        requests_new = self.env['request.request'].search(
            [('id', 'not in', requests_before.ids)])
        return requests_new
