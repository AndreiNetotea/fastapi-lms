import fastapi

router = fastapi.APIRouter()

@router.get("/sections/{section_id}")
async def read_section(section_id: int):
    return {"section": {}}


@router.get("/sections/{section_id}/content-blocks")
async def read_section_content_blocks(section_id: int):
    return {"content_blocks": []}

@router.get("/content-blocks/{content_block_id}")
async def read_content_block(content_block_id: int):
    return {"content_block": {}}
