from voluptuous import PREVENT_EXTRA, Schema

get_list_dogs = Schema(
    {
        "message": {
            "affenpinscher": [],
            "african": [],
            "airedale": [],
            "akita": [],
            "appenzeller": [],
            "australian": [str],
            "basenji": [],
            "beagle": [],
            "bluetick": [],
            "borzoi": [],
            "bouvier": [],
            "boxer": [],
            "brabancon": [],
            "briard": [],
            "buhund": [str],
            "bulldog": [str, str, str],
            "bullterrier": [str],
            "cattledog": [str],
            "chihuahua": [],
            "chow": [],
            "clumber": [],
            "cockapoo": [],
            "collie": [str],
            "coonhound": [],
            "corgi": [str],
            "cotondetulear": [],
            "dachshund": [],
            "dalmatian": [],
            "dane": [str],
            "deerhound": [str],
            "dhole": [],
            "dingo": [],
            "doberman": [],
            "elkhound": [str],
            "entlebucher": [],
            "eskimo": [],
            "finnish": [str],
            "frise": [str],
            "germanshepherd": [],
            "greyhound": [str],
            "groenendael": [],
            "havanese": [],
            "hound": [
                str,
                str,
                str,
                str,
                str,
                str,
                str,
            ],
            "husky": [],
            "keeshond": [],
            "kelpie": [],
            "komondor": [],
            "kuvasz": [],
            "labradoodle": [],
            "labrador": [],
            "leonberg": [],
            "lhasa": [],
            "malamute": [],
            "malinois": [],
            "maltese": [],
            "mastiff": [str, str, str],
            "mexicanhairless": [],
            "mix": [],
            "mountain": [str, str],
            "newfoundland": [],
            "otterhound": [],
            "ovcharka": [str],
            "papillon": [],
            "pekinese": [],
            "pembroke": [],
            "pinscher": [str],
            "pitbull": [],
            "pointer": [str, str],
            "pomeranian": [],
            "poodle": [
                str,
                str,
                str,
                str,
            ],
            "pug": [],
            "puggle": [],
            "pyrenees": [],
            "redbone": [],
            "retriever": [
                str,
                str,
                str,
                str,
            ],
            "ridgeback": [
                str,
            ],
            "rottweiler": [],
            "saluki": [],
            "samoyed": [],
            "schipperke": [],
            "schnauzer": [
                str,
                str,
            ],
            "segugio": [
                str,
            ],
            "setter": [
                str,
                str,
                str,
            ],
            "sharpei": [],
            "sheepdog": [
                str,
                str,
            ],
            "shiba": [],
            "shihtzu": [],
            "spaniel": [
                str,
                str,
                str,
                str,
                str,
                str,
                str,
            ],
            "spitz": [
                str,
            ],
            "springer": [
                str,
            ],
            "stbernard": [],
            "terrier": [
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
            ],
            "tervuren": list,
            "vizsla": list,
            "waterdog": list,
            "weimaraner": list,
            "whippet": list,
            "wolfhound": list,
        },
        "status": str,
    },
    extra=PREVENT_EXTRA,
    required=True,
)


list_all_sub_breeds = Schema(
    {"message": [str, str, str, str, str, str, str], "status": str},
    extra=PREVENT_EXTRA,
    required=True,
)
