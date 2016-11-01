from pysettings import conf
from pythonvideoannotator.models.objects.object2d.object2d_gui 			import Object2dGUI as BaseObject2d
from pythonvideoannotator.models.objects.object2d.utils.interpolation 	import interpolate_positions


Object2d = type(
	'Object2d',
	tuple(conf.MODULES.find_class('models.objects.object2d.Object2d') + [BaseObject2d]),
	{}
)