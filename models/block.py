from enum import IntEnum


class BlockType(IntEnum):
    INVALID = 0
    NOT_A_BLOCK = 1
    SEND = 2
    RECEIVE = 3
    OPEN = 4
    CHANGE = 5


class Block:
    def __init__(self, block_type):
        self.block_type = block_type

    def to_bytes(self):
        return bytes([self.block_type.value])


class BlockParser:
    @staticmethod
    def parse(data: bytes) -> Block:
        block_type: BlockType = BlockType(data[0])
        if block_type == BlockType.SEND:
            pass
        elif block_type == BlockType.RECEIVE:
            pass
        elif block_type == BlockType.OPEN:
            pass
        elif block_type == BlockType.CHANGE:
            pass
        else:
            pass

        return Block(block_type)
