from avatar_generator import AvatarGenerator


def generate_avatar():
    generator = AvatarGenerator("./collections/crypto_punk")
    generator.generate_avatar(100)


if __name__ == "__main__":
    generate_avatar()
