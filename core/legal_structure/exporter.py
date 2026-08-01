from core.legal_structure.models.nodes import LegalNode


def node_to_dict(node: LegalNode):

    return {
        "type": node.node_type,
        "title": node.title,
        "number": node.number,
        "text": node.text,
        "children": [node_to_dict(child) for child in node.children],
    }
