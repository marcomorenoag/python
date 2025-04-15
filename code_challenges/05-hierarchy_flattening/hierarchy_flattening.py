"""
Hierarchy Flattening
Given a dictionary your task is to flatten the Hierarchy the following ways:
If there is a nested structure the parent key should be concatenated to the child keys.
If there is a primitive type the key shouldn't be changed.
Input:
{
 'a': 1,
 'b': 'foo',
 'c': {
   'a': 2,
   'b': 'bar'
 }
}
Output:
{
 'a': 1,
 'b': 'foo',
 'c_a': 2,
 'c_b' : 'bar',
}
"""


def flatten(input_object, parent_key=""):
    processed_object = {}
    object_keys = input_object.keys()

    for key in object_keys:
        current_value = input_object[key]
        if isinstance(current_value, dict):
            ancestors_parent_keys = f"{parent_key}{key}_" if parent_key else f"{key}_"
            processed_object = {
                **processed_object,
                **flatten(current_value, ancestors_parent_keys),
            }
        else:
            processed_object[f"{parent_key}{key}"] = current_value
    return processed_object


if __name__ == "__main__":
    example_one = {
        "a": 1,
        "b": "foo",
        "c_a": "a thing",
        "c": {
            "a": 2,
            "b": {"a": 4, "b": "bar"},
        },
    }
    result = flatten(example_one)
    print(result)


# # Linux tech questions
# # What next line does?
#     chmod 664 myfile
# # How search next key text into a project? Hint: grep
#     my_func
