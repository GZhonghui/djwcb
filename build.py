# 解析数据文件！生成Vue的代码
# index.js + all views

import os,json

# 删除文件，本函数由AI生成
def delete_all_files_in_directory(directory_path):
  # Check if the path exists
  if not os.path.exists(directory_path):
    print(f"The directory {directory_path} does not exist.")
    return
  
  # Iterate over all files and folders in the directory
  for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    try:
      # Check if it is a file
      if os.path.isfile(file_path) or os.path.islink(file_path):
        os.remove(file_path)  # Delete the file or symbolic link
      elif os.path.isdir(file_path):
        # If it is a folder and you want to delete its contents, you can recursively delete
        delete_all_files_in_directory(file_path)
        os.rmdir(file_path)  # Delete the empty folder
    except Exception as e:
      print(f"Failed to delete {file_path}. Reason: {e}")

def read_template(file_path: str) -> list:
  with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    return [line.rstrip('\n') for line in lines]

def write_code(code: list, begin_line: int, end_line: int) -> str:
  result = str()
  for line_id in range(begin_line, end_line + 1):
    result = result + code[line_id-1] + '\n'
  return result

def read_data() -> list:
  data, game_to_id, id_to_game, game_id, contain_dates = dict(), dict(), dict(), 0, dict()
  data_files = sorted([i for i in os.listdir('./data/') if i.split('.')[-1] == 'json'])
  for file_name in data_files:
    with open(os.path.join('./data/',file_name), 'r', encoding='utf-8') as file:
      json_data = json.load(file)
      for date in json_data.keys():
        if len(json_data[date]['games']) > 0:
          for game_data in json_data[date]['games']:
            game = game_data if isinstance(game_data, str) else game_data[0]
            if game not in data.keys():
              data[game], contain_dates[game] = list(), dict()
              game_id = game_id + 1
              game_to_id[game],id_to_game[game_id] = game_id,game
            complate_date = date if isinstance(game_data, str) else f'{date}[{game_data[1]}]'
            if complate_date not in contain_dates[game].keys():
              data[game].append([complate_date,json_data[date]['url']])
              contain_dates[game][complate_date] = 1
  return data, game_to_id, id_to_game

def main():
  name_zero_fill_count = 4
  data, game_to_id, id_to_game = read_data()
  index_js_code = read_template('./template/index.js')
  views_vue_code = read_template('./template/views.vue')
  delete_all_files_in_directory('./vue-project/src/views/')

  # 注意，这是一个危险的操作，ID强制填充0后，得到的ID不能再用于索引反向得到Game
  for k in game_to_id.keys():
    game_to_id[k] = str(game_to_id[k]).zfill(name_zero_fill_count)

  with open('./vue-project/src/router/index.js', 'w', encoding='utf-8') as file:
    file.write(write_code(index_js_code,3,4))
    for game in data.keys():
      file.write(f'import GameView{game_to_id[game]} from \'../views/GameView{game_to_id[game]}.vue\';\n')
    file.write(write_code(index_js_code,6,11))
    for game in data.keys():
      file.write(f'{{path: \'/game{game_to_id[game]}\', name: \'GameView{game_to_id[game]}\', component: GameView{game_to_id[game]}}},\n')
    file.write(write_code(index_js_code,12,19))

  with open('./vue-project/src/views/AllGames.vue', 'w', encoding='utf-8') as file:
    file.write(write_code(views_vue_code,3,22))
    for game in data.keys():
      file.write(f'"{game}": "/game{game_to_id[game]}",\n')
    file.write(write_code(views_vue_code,24,41))

  for game in data.keys():
    with open(f'./vue-project/src/views/GameView{game_to_id[game]}.vue', 'w', encoding='utf-8') as file:
      file.write(write_code(views_vue_code,3,22))
      # file.write(f'"回到首页": "/",\n')
      for date in data[game]:
        file.write(f'"{date[0]}": "{date[1]}",\n')
      file.write(write_code(views_vue_code,24,41))

if __name__ == '__main__':
  main()