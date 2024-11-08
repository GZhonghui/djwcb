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
  data, game_to_id, id_to_game, game_id = dict(), dict(), dict(), 0
  data_files = [i for i in os.listdir('./data/') if i.split('.')[-1] == 'json']
  for file_name in data_files:
    with open(os.path.join('./data/',file_name), 'r', encoding='utf-8') as file:
      json_data = json.load(file)
      for date in json_data.keys():
        if len(json_data[date]['games']) > 0:
          for game in json_data[date]['games']:
            if game not in data.keys():
              data[game] = list()
              game_id = game_id + 1
              game_to_id[game],id_to_game[game_id] = game_id,game
            data[game].append([date,json_data[date]['url']])
  return data, game_to_id, id_to_game

def main():
  data, game_to_id, id_to_game = read_data()
  index_js_code = read_template('./template/index.js')
  views_vue_code = read_template('./template/views.vue')
  delete_all_files_in_directory('./vue-project/src/views/')

  with open('./vue-project/src/router/index.js', 'w', encoding='utf-8') as file:
    file.write(write_code(index_js_code,3,4))
    for game in data.keys():
      file.write(f'import GaMe{game_to_id[game]} from \'../views/GaMe{game_to_id[game]}.vue\';\n')
    file.write(write_code(index_js_code,6,11))
    for game in data.keys():
      file.write(f'{{path: \'/game{game_to_id[game]}\', name: \'GaMe{game_to_id[game]}\', component: GaMe{game_to_id[game]}}},\n')
    file.write(write_code(index_js_code,12,19))

  with open('./vue-project/src/views/AllGames.vue', 'w', encoding='utf-8') as file:
    file.write(write_code(views_vue_code,3,22))
    for game in data.keys():
      file.write(f'"{game}": "/game{game_to_id[game]}",\n')
    file.write(write_code(views_vue_code,24,77))

  for game in data.keys():
    with open(f'./vue-project/src/views/GaMe{game_to_id[game]}.vue', 'w', encoding='utf-8') as file:
      file.write(write_code(views_vue_code,3,22))
      file.write(f'"回到首页": "/",\n')
      for date in data[game]:
        file.write(f'"{date[0]}": "{date[1]}",\n')
      file.write(write_code(views_vue_code,24,77))

if __name__ == '__main__':
  main()