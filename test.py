def generate_new_paths(file_paths, context_name):
    """
    使用 ChatGPT 生成符合 Emby 标准的新路径
    :param file_paths: 文件绝对路径列表
    :param context_name: 当前目录名（影视名称）
    :return: 一个字典，{原路径: 新路径}
    """
    movie_dir_name = "电影"
    tv_dir_name = "电视剧"
    anime_dir_name = "动漫"
    prompt = f"""
    我有一个名为 的影视资源目录，里面存放着电影、电视剧和动漫。请根据以下 Emby 命名规范，为每个文件生成符合规范的新文件绝对路径。
    **Emby 命名规范：**
    *   **电影：**
        *   格式：`电影目录/电影名称 (年份).扩展名`
        *   电影目录名称： (默认为"电影")
        *   电影名称和年份之间用空格和半角括号分隔。
        *   如果文件名中已包含年份，请尽量使用原有年份。
        *   如果存在多个版本（如导演剪辑版），请在年份后添加版本信息，例如：`电影名称 (年份) 导演剪辑版.扩展名`
    *   **电视剧：**
        *   格式：`电视剧目录/剧集名称/Season 季号/剧集名称 - S季号E集号 - 集标题(可选).扩展名`
        *   电视剧目录名称 (默认为"电视剧")
        *   季号和集号必须为两位数，不足两位前面补零。例如：`S01E01`
        *   剧集名称、季号、集号之间用空格和半角短横线 `-` 分隔。
        *   如果文件名中已包含季号和集号，请尽量使用原有信息。
        *   特殊剧集（如SP、OVA）放在 `Specials` 文件夹中，并使用 `S00E集号` 的格式。
    *   **动漫：**
        *   格式：`动漫目录/动漫名称/Season 季号/动漫名称 - Ep 集号.扩展名`
        *   动漫目录名称：(默认为"动漫")
        *   季号为两位数，不足两位前面补零。集号可以是一位或多位。
        *   动漫名称、季号、集号之间用空格和半角短横线 `-` 分隔。
        *   如果文件名中已包含季号和集号，请尽量使用原有信息。
        *   特殊剧集（如SP、OVA）放在 `Specials` 文件夹中，并使用 `Ep 特殊集号` 的格式,例如：`Ep01`。

    **文件列表：**
    **要求：**
    1. 请根据文件路径和名称，推断其属于电影、电视剧还是动漫。
    2. 如果无法识别，请将其原路径添加到名为 "unidentified" 的键值对中。
    3. 如果下还有子文件夹，请递归的向下遍历。
    4. 返回一个 **纯净的** JSON 格式字典，**不要包含任何其他字符**，例如说明文字、换行符等。字典格式如下：
    [{{
        "旧文件绝对路径": "新文件绝对路径",
    }}]
"""
    print(prompt)

generate_new_paths("123", "12")