# global
import numpy as np
from hypothesis import given, strategies as st

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy.functional.backends.numpy as ivy_np
import ivy_tests.test_ivy.test_frontends.test_numpy.helpers as np_frontend_helpers


# mean
@given(
    dtype_and_a=helpers.dtype_and_values(
        available_dtypes=ivy_np.valid_float_dtypes
    ),
    dtype=st.sampled_from(ivy_np.valid_float_dtypes + (None,)),
    where=np_frontend_helpers.where(),
    as_variable=helpers.array_bools(num_arrays=1),
    with_out=st.booleans(),
    num_positional_args=helpers.num_positional_args(
        fn_name="ivy.functional.frontends.numpy.mean"
    ),
    native_array=helpers.array_bools(num_arrays=1),
)
def test_numpy_mean(
    dtype_and_a,
    dtype,
    with_out,
    where,
    as_variable,
    num_positional_args,
    native_array,
    fw,
):
    input_dtype, a = dtype_and_a
    where = np_frontend_helpers.handle_where_and_array_bools(
        where=where,
        input_dtype=[input_dtype],
        as_variable=as_variable,
        native_array=native_array,
    )
    np_frontend_helpers.test_frontend_function(
        input_dtypes=input_dtype,
        as_variable_flags=as_variable,
        with_out=with_out,
        num_positional_args=num_positional_args,
        native_array_flags=native_array,
        fw=fw,
        frontend="numpy",
        fn_tree="mean",
        a=np.asarray(a, dtype=input_dtype[0]),
        axis=None,
        dtype=dtype,
        out=None,
        keepdims=False,
        where=where,
    )
