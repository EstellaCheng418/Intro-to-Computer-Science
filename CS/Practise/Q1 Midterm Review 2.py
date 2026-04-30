# Q1 Midterm Review 2
letters = "AhVpXuCoMAlPzeILmIyNXgdRlVUwKtCzIOHuCLNKDVOdeqwnjQmhJkAbym\
kBkUQVhxrpPRosUcvHvfMSEGaTVmNJRISIREDkOVGkTizAsGeVyewaSSabK\
ICCHWgUrXxvYfYCnVcaOwIPmvGDSFdeTFBYYrwiLaxRciFjNRnelIZtMbvr\
RNuRENUMSOsgUxkwAvdaTQBiLFQjdyHPmDMDsSjwbBOOplHYHfqLDNUFlWA\
UdPgeIqqDXmuPAuFsLgtNpWibgtVqJkqDnzJILyrXwWXroImXCGfewQMZnm\
QPmKKchPTsihPozppbUGOcJIiCKmbaVQaQEtDCeARSRvCcOGeyTaNDGyZqz\
UWcARuNUQcsRQYTGyrkLrVwSsjGVhGGLujVuyxqxECJdjsj"

vowels = "AEIOUaeiou"

not_vowels = 0
for char in letters:
    if char not in vowels:
        not_vowels += 1
print("Number of characters that are not vowels:", not_vowels)
