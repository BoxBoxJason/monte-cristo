from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/{graph_name}")
async def getGraph(graph_name: str):
    if graph_name == "line_chart":
        return JSONResponse(content={
            "xAxis": {
                "type": "category",
                "data": ["January", "February", "March", "April"]
            },
            "yAxis": {
                "type": "value"
            },
            "series": [
                {
                    "name": "Dataset 1",
                    "type": "line",
                    "data": [65, 59, 80, 81],
                    "lineStyle": {
                        "color": "#FF0000"
                    },
                    "smooth": True
                }
            ]
        })
    elif graph_name == "bar_chart":
        return JSONResponse(content={
            "xAxis": {
                "type": "category",
                "data": ["Red", "Blue", "Yellow", "Green"]
            },
            "yAxis": {
                "type": "value"
            },
            "series": [
                {
                    "name": "Dataset 1",
                    "type": "bar",
                    "data": [12, 19, 3, 5],
                    "itemStyle": {
                        "color": ["rgba(255, 99, 132, 0.2)", "rgba(54, 162, 235, 0.2)", "rgba(255, 206, 86, 0.2)", "rgba(75, 192, 192, 0.2)"],
                        "borderColor": ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)", "rgba(255, 206, 86, 1)", "rgba(75, 192, 192, 1)"],
                        "borderWidth": 1
                    }
                }
            ]
        })
    elif graph_name == "pie_chart":
        return JSONResponse(content={
            "series": [
                {
                    "name": "Dataset",
                    "type": "pie",
                    "radius": "50%",
                    "data": [
                        {"value": 300, "name": "Red", "itemStyle": {"color": "#FF6384"}},
                        {"value": 50, "name": "Blue", "itemStyle": {"color": "#36A2EB"}},
                        {"value": 100, "name": "Yellow", "itemStyle": {"color": "#FFCE56"}}
                    ]
                }
            ]
        })
    else:
        return JSONResponse(content={"error": "Graph not found"}, status_code=404)
