
import tensorflow as tf

__all__ = ['get_default_session_config']

def get_default_session_config(memory_fraction = 1):
	conf = tf.ConfigProto()

	conf.gpu_options.per_process_gpu_memory_fraction = memory_fraction
	conf.gpu_options.allow_growth = True

	return conf