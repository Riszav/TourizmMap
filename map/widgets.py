from django import forms
from django.utils.safestring import mark_safe

class LeafletWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',
            )
        }
        js = (
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.js',
        )

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        leaflet_map = '''
            <div id="map" style="height: 400px; width: 100%;"></div>
            <script type="text/javascript">
                document.addEventListener('DOMContentLoaded', function () {
                    var map = L.map('map').setView([42.86969106012299, 74.58479679498225], 7);
                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '© OpenStreetMap contributors'
                    }).addTo(map);
                    var marker;
                    var latInput = document.getElementsByName("latitude")[0];
                    var lngInput = document.getElementsByName("longitude")[0];
                    if (latInput.value && lngInput.value) {
                        var initialLatLng = [parseFloat(latInput.value), parseFloat(lngInput.value)];
                        map.setView(initialLatLng, 7);
                        marker = L.marker(initialLatLng).addTo(map);
                    }
                    map.on('click', function(e) {
                        if (marker) {
                            marker.setLatLng(e.latlng);
                        } else {
                            marker = L.marker(e.latlng).addTo(map);
                        }
                        latInput.value = e.latlng.lat;
                        lngInput.value = e.latlng.lng;
                    });
                });
            </script>
        '''
        return mark_safe(html + leaflet_map)
