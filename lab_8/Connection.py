class Connection(object):
    def __init__(self, input_node, output_node):
        self._input_node = input_node
        self._output_node = output_node
        self._signal_power = None
        self._latency = 0
        self._snr = 0
        self._bitrate = None

    @property
    def input_node(self):
        return self._input_node

    @property
    def bitrate(self):
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        self._bitrate = bitrate

    @property # make sure about this
    def calculate_capacity(self):
        return self._bitrate

    @property
    def output_node(self):
        return self._output_node

    @property
    def signal_power(self):
        return self._signal_power

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def latency(self, latency):
        self._latency = latency

    @signal_power.setter
    def signal_power(self, signal_power):
        self._signal_power = signal_power

    @property
    def snr(self):
        return self._snr

    @snr.setter
    def snr(self, snr):
        self._snr = snr